provider "time" {}

provider "http" {}

resource "time_static" "timestamp" {}

data "http" "example_get" {
  url    = "https://gateway.marvel.com/v1/public/characters?ts=${time_static.timestamp.unix}&apikey=${var.pub_key}&hash=${local.hash}&name=Hulk"
  method = "GET"
}


