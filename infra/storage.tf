resource "aws_s3_bucket" "random_files" {
  bucket = "${local.ns}-random-files"
}

# Make the bucket private
resource "aws_s3_bucket_public_access_block" "random_files" {
  bucket = aws_s3_bucket.random_files.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
