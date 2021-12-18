'''
This program uses breadth-first search in order to look at the min degrees of separation between
two connected addresses on Ethereum

By: Christopher Pondoc
'''
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import json

# Global variables
source_addr = "0x8ddD03b89116ba89E28Ef703fe037fF77451e38E"
#target_addr = "0x0c78df329571a4f08d4e9a9d627f6e099721978d"
target_addr = "0xb7706727afb71d0a1f617f62c29df36b86649999"

# Set up call to query
def set_up_query():
    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="https://api.cybertino.io/connect/")

    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

# Create GraphQL Query
def create_query(client, selected_addr):
    # Provide a GraphQL query
    query = gql(
        """
        query {
        # ENS can also be passed as the address here to fetch idenity.
        identity(address: \"""" + selected_addr + """\") {
            address
            followingCount
            followerCount
            followers {
            list {
                address
            }
            }
            followings {
            list{
                address
            }
            }
        }
    }
    """
    )

    # Execute the next query on the transport
    result = client.execute(query)
    followers = result['identity']['followers']['list']
    return followers

# Use Breadth-First Search in order to find path
def graph_bfs(client, source, target):
    # Set up visited addresses and list of all lists
    visited_addr = []
    all_lists = []

    # Create initial list
    initial_list = [source]
    visited_addr.append(source)
    all_lists.append(initial_list)
    
    while all_lists:
        # Pop the current list and get the last element in the list
        current_list = all_lists.pop(0)
        last_addr = current_list[len(current_list) - 1]

        # Look at all following addresses
        addr_followers = create_query(client, last_addr)
        for new_followers in addr_followers:
            # Extract new address and check if not already visited
            new_follower = new_followers['address']
            if (new_follower not in visited_addr):
                # Add it to queue of things to look at, and also return new
                visited_addr.append(new_follower)
                new_list = current_list.copy()
                new_list.append(new_follower)
                all_lists.append(new_list)
                if (new_follower == target):
                    return new_list

# Run code and check
client = set_up_query()
final_list = graph_bfs(client, source_addr, target_addr)
print(final_list)