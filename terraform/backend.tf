terraform {
  backend "s3" {
    bucket = "htl-datalake-deploy-dev"
    key    = "htl-intern-bucket/terraform.tfstate"
    region = "ap-northeast-1"
  }
}
