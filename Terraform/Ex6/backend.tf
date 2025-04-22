terraform {
  backend "s3" {
    bucket = "terraformstate123" #bucket name
    key = "terraform/backend" #folder/filename
    region = "us-east-1"
  }
}