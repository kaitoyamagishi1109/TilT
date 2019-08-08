resource "aws_s3_bucket" "b1" {
  bucket = "htl-intern-work"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  logging {
    target_bucket = "${aws_s3_bucket.log.id}"
    target_prefix = "log/"
  }
}

resource "aws_s3_bucket" "log" {
  bucket = "htl-intern-log"
  acl    = "log-delivery-write"
}
