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

resource "aws_s3_bucket_policy" "b1" {
  bucket = "${aws_s3_bucket.b1.id}"

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::htl-intern-work/*"
        }
    ]
}
POLICY
}


resource "aws_s3_bucket" "log" {
  bucket = "htl-intern-log"
  acl    = "log-delivery-write"
}

resource "aws_s3_bucket_object" "file_upload1" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "index.html"
  content_type = "text/html"
  source = "../html/index.html"
}
resource "aws_s3_bucket_object" "file_upload2" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "error.html"
  content_type = "text/html"
  source = "../html/error.html"
}
