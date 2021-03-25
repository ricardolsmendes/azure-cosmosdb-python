import argparse
from argparse import Namespace
import json
import logging
import sys
from typing import Dict, List
import uuid

from azure import cosmos
from azure.cosmos import ContainerProxy, CosmosClient, DatabaseProxy


def __parse_args(exec_args: List[str]) -> Namespace:
    parser = argparse.ArgumentParser(
        description='Command-line utility to upload JSON-formatted data to'
                    ' Azure Cosmos DB')

    parser.add_argument('--cosmos-endpoint',
                        help='The Cosmos DB endpoint', required=True)
    parser.add_argument('--cosmos-key',
                        help='The Cosmos DB key', required=True)
    parser.add_argument('--cosmos-database',
                        help='The Cosmos DB database id', required=True)
    parser.add_argument('--cosmos-container',
                        help='The Cosmos DB container id', required=True)
    parser.add_argument('--partition-key',
                        help='The partition key', required=True)
    parser.add_argument('--data',
                        help='JSON content to be persisted', required=True)

    return parser.parse_args(exec_args)


def __init_cosmos_client(endpoint: str, key: str) -> CosmosClient:
    return cosmos.CosmosClient(endpoint, key)


def __init_cosmos_database(
        database_id: str, cosmos_client: CosmosClient) -> DatabaseProxy:

    return cosmos_client.create_database_if_not_exists(id=database_id)


def __init_cosmos_container(
        container_id: str, partition_key: str, database_proxy: DatabaseProxy)\
        -> ContainerProxy:

    return database_proxy.create_container_if_not_exists(
        id=container_id, partition_key=cosmos.PartitionKey(path=partition_key))


def __persist_json_data(
        data: Dict, cosmos_container: ContainerProxy) -> Dict[str, str]:

    return cosmos_container.create_item(body=data)


if __name__ == "__main__":
    argv = sys.argv
    args = __parse_args(argv[1:] if len(argv) > 0 else argv)

    client = __init_cosmos_client(args.cosmos_endpoint, args.cosmos_key)
    database = __init_cosmos_database(args.cosmos_database, client)
    container = __init_cosmos_container(
        args.cosmos_container, args.partition_key, database)

    json_data = json.loads(args.data)
    json_data['id'] = str(uuid.uuid4())

    logging.info(__persist_json_data(json_data, container))
