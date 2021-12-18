# Degrees of Separation
Experimentation with degrees of separation between different ETH addresses on the CybcerConnect network.

## Motivation
CyberConnect is building cool technology within Web3 that essentially connect everyone via a social graph. Due to my interest in network science, I was curious to see how to calculate *degrees of separation* within these networks. Specifically, I wanted to see just how far two Ethereum addresses would be.

## Implementation
This program uses the CyberConnect GraphQL API in order to generate the followers list for a specific ETH address. From there, I implement a breadth-first search to find (one of the) shortest paths.

### To-Do
-Add parser args/make customizable
-Some visual implementation on top?

## To Run
```python
python3 main.py
```