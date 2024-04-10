# templates/aws/s3_bucket.tpl

resource "aws_s3_bucket" "tanni-20" {
  bucket = "tanni-20"
  acl    = "private"
  
}