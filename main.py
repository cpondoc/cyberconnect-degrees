from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport
import json

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="https://api.cybertino.io/connect/")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)
original_addr = "0x8ddD03b89116ba89E28Ef703fe037fF77451e38E"


# Provide a GraphQL query
query = gql(
    """
    query {
  # ENS can also be passed as the address here to fetch idenity.
  identity(address: \"""" + original_addr + """\") {
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

# Execute the query on the transport
result = client.execute(query)
next_addr = ""
followers = result['identity']['followers']['list']
print(original_addr + " Followers:")
for follower in followers:
    next_addr = follower['address']
    print(follower)


# Provide a second GraphQL query
query = gql(
    """
    query {
  # ENS can also be passed as the address here to fetch idenity.
  identity(address: \"""" + next_addr + """\") {
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
print("\n" + next_addr + " Followers:")
for follower in followers:
    next_addr = follower['address']
    print(follower)