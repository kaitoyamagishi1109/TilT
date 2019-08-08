provider "aws" {
  region = "ap-northeast-1"
}

variable "msa_role" {
    description = "msa role"
    default = "arn:aws:iam::703622364183:role/msarole"
}
