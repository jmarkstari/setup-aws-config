

if __name__ == "__main__":

    lambda_function_name = ""
    aws_account_number = ""
    subnet_ids = ""
    sec_group_id = ""
    neptune_cluster_endpoint = ""
    neptune_db_port = ""

    command_fstr = f"""
    aws lambda create-function --function-name {lambda_function_name} \
    --role "arn:aws:iam::{aws_account_number}:role/service-role/lambda-vpc-access-role" \
    --runtime python3.6 --handler configparser_lambdafunction.lambda_handler \
    --description "Lambda function to parse AWS Config and make gremlin calls to Amazon Neptune" \
    --timeout 120 --memory-size 256 --publish \
    --vpc-config SubnetIds={subnet_ids},SecurityGroupIds={sec_group_id} \
    --zip-file fileb://function.zip \
    --environment Variables="{{CLUSTER_ENDPOINT={neptune_cluster_endpoint},CLUSTER_PORT={neptune_db_port}}}"
    """

    print(command_fstr)