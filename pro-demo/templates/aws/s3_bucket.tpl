# templates/aws/s3_bucket.tpl

resource "aws_s3_bucket" "{{ bucket_name }}" {
  bucket = "{{ bucket_name }}"
  acl    = "{{ acl }}"
  
}
