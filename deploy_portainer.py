#!/usr/bin/python
import sys, os
import portainer
import argparse

def authentication(configuration, username, password):
    api_instance = portainer.AuthApi(portainer.ApiClient(configuration))
    body = portainer.AuthAuthenticatePayload(password=password, username=username)
    api_response = api_instance.authenticate_user(body)
    configuration.api_key['Authorization'] = api_response.jwt
    print("Authenticated successfully")

def update_stack(configuration, stack_id, endpoint_id, compose_file):
    api_instance = portainer.StacksApi(portainer.ApiClient(configuration))
    with open(compose_file,"r") as f:
        compose_content = f.read()
        api_response = api_instance.stack_update(id=stack_id, body={"stackFileContent":compose_content}, endpoint_id=endpoint_id)
        print("Deployed successfully")

def deploy(host, username, password, stack_id, endpoint_id, compose_file):
    configuration = portainer.Configuration()
    configuration.host = host
    authentication(configuration, username, password)
    update_stack(configuration, stack_id, endpoint_id, compose_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deploy stack')
    parser.add_argument('--host', type=str)
    parser.add_argument('--username', type=str)
    parser.add_argument('--password', type=str)
    parser.add_argument('--stack_id', type=str)
    parser.add_argument('--endpoint_id', type=str)
    parser.add_argument('--compose_file', type=str)
    args = parser.parse_args()
    deploy(args.host, args.username, args.password, args.stack_id, args.endpoint_id, args.compose_file)
