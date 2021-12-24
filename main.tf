variable "url" {}

data "external" "parse" {
  program = ["python3", "${path.module}/url2json.py", chomp(var.url)]
}

output "scheme" {
  value = data.external.parse.result.scheme
}

output "username" {
  value = data.external.parse.result.username
}

output "password" {
  value = data.external.parse.result.password
  sensitive = true
}

output "hostname" {
  value = data.external.parse.result.hostname
}

output "port" {
  value = data.external.parse.result.port
}

output "path" {
  value = data.external.parse.result.path
}

output "query" {
  value = data.external.parse.result.query
}

output "fragment" {
  value = data.external.parse.result.fragment
}

output "netloc" {
  value = data.external.parse.result.netloc
}
