output "http_response" {
  value = data.http.example_get
}

output "current_time" {
  value = time_static.timestamp.unix
}