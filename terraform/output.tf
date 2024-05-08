output "http_response" {
  value     = data.http.example_get.response_body
  sensitive = false
}

output "current_time" {
  value = time_static.timestamp.unix
}