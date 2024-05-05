locals {
  hash = md5(format("%s%s%s",time_static.timestamp.unix,var.pri_key,var.pub_key))
}