provider "aws" {
  region = "ap-northeast-1"
}

variable "msa_role" {
    description = "msa role"
    default = "arn:aws:iam::589021901386:role/msarole"
}
