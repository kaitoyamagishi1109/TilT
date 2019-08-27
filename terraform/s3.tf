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
  etag = "${filemd5("../html/index.html")}"
}
resource "aws_s3_bucket_object" "file_upload2" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "error.html"
  content_type = "text/html"
  source = "../html/error.html"
  etag = "${filemd5("../html/error.html")}"
}
resource "aws_s3_bucket_object" "file_upload3" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "east.png"
  content_type = "image/png"
  source = "../html/east.png"
  etag = "${filemd5("../html/east.png")}"
}
resource "aws_s3_bucket_object" "file_upload4" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "west.png"
  content_type = "image/png"
  source = "../html/west.png"
  etag = "${filemd5("../html/west.png")}"
}
resource "aws_s3_bucket_object" "file_upload5" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "train_east.png"
  content_type = "image/png"
  source = "../html/train_east.png"
  etag = "${filemd5("../html/train-east.png")}"
}
resource "aws_s3_bucket_object" "file_upload6" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "train_west.png"
  content_type = "image/png"
  source = "../html/train_west.png"
  etag = "${filemd5("../html/train-west.png")}"
}
resource "aws_s3_bucket_object" "file_upload7" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "empty.png"
  content_type = "image/png"
  source = "../html/empty.png"
  etag = "${filemd5("../html/empty.png")}"
}
resource "aws_s3_bucket_object" "file_upload8" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "eastbound-1.png"
  content_type = "image/png"
  source = "../html/eastbound-1.png"
  etag = "${filemd5("../html/eastbound-1.png")}"
}
resource "aws_s3_bucket_object" "file_upload9" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "eastbound-2.png"
  content_type = "image/png"
  source = "../html/eastbound-2.png"
  etag = "${filemd5("../html/eastbound-2.png")}"
}
resource "aws_s3_bucket_object" "file_upload10" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "eastbound-3.png"
  content_type = "image/png"
  source = "../html/eastbound-3.png"
  etag = "${filemd5("../html/eastbound-3.png")}"
}
resource "aws_s3_bucket_object" "file_upload11" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "eastbound-4.png"
  content_type = "image/png"
  source = "../html/eastbound-4.png"
  etag = "${filemd5("../html/eastbound-4.png")}"
}
resource "aws_s3_bucket_object" "file_upload12" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "eastbound-5.png"
  content_type = "image/png"
  source = "../html/eastbound-5.png"
  etag = "${filemd5("../html/eastbound-5.png")}"
}
resource "aws_s3_bucket_object" "file_upload13" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "westbound-1.png"
  content_type = "image/png"
  source = "../html/westbound-1.png"
  etag = "${filemd5("../html/westbound-1.png")}"
}
resource "aws_s3_bucket_object" "file_upload14" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "westbound-2.png"
  content_type = "image/png"
  source = "../html/westbound-2.png"
  etag = "${filemd5("../html/westbound-2.png")}"
}
resource "aws_s3_bucket_object" "file_upload15" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "westbound-3.png"
  content_type = "image/png"
  source = "../html/westbound-3.png"
  etag = "${filemd5("../html/westbound-3.png")}"
}
resource "aws_s3_bucket_object" "file_upload16" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "westbound-4.png"
  content_type = "image/png"
  source = "../html/westbound-4.png"
  etag = "${filemd5("../html/westbound-4.png")}"
}
resource "aws_s3_bucket_object" "file_upload17" {
  bucket = "${aws_s3_bucket.b1.id}"
  key    = "westbound-5.png"
  content_type = "image/png"
  source = "../html/westbound-5.png"
  etag = "${filemd5("../html/westbound-5.png")}"
}
    
