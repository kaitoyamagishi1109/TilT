data "archive_file" "lambda_function" {
  type        = "zip"
  source_dir  = "../src"
  output_path = "./src.zip"
}

resource "aws_lambda_function" "api" {
  function_name = "TrainApi"

  filename         = "${data.archive_file.lambda_function.output_path}"
  source_code_hash = "${data.archive_file.lambda_function.output_base64sha256}"

  handler = "main.lambda_handler"
  runtime = "python3.6"

  role = "${var.msa_role}"
}

resource "aws_lambda_permission" "apigw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.api.arn}"
  principal     = "apigateway.amazonaws.com"

  # The /*/* portion grants access from any method on any resource
  # within the API Gateway "REST API".
  source_arn = "${aws_api_gateway_deployment.api.execution_arn}/*/*"
}
