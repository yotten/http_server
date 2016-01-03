#!/home/pi/.rbenv/shims/ruby
# -*- coding: utf-8 -*-

def checkGET
  str = ENV["QUERY_STRING"]
  ary = str.split("&")
  @forms = {}

  ary.each do |obj|
    datas = obj.split("=")
    @forms.store(datas[0], datas[1])
  end

  @str = str
end

def writeHTML
  puts "Content-Type: text/html"
  puts
  puts "<html><head>"
  puts "<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">"
  puts "</head><body>"
  puts "<h3>こんにちは。</h3>"
  puts "<p>これはCGIプログラムからの表示です。</p>"
  puts "あなたは、「" + @forms['text1'] + "」と書いたね？"
  puts @str 
  puts "</body></html>"
end

checkGET
writeHTML

