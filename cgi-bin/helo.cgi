#!/home/pi/.rbenv/shims/ruby
# -*- coding: utf-8 -*-
require "cgi"

def writeHTML
  puts "Content-Type: text/html"
  puts
  puts "<html><head>"
  puts "<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">"
  puts "</head><body>"
  puts "<h3>こんにちは。</h3>"
  puts "<p>これはCGIプログラムからの表示です。</p>"
  puts "あなたは、「" + @cgi['text1'] + "」と書いたね？"
#  puts @str 
  puts "</body></html>"
end

@cgi = CGI.new
writeHTML

