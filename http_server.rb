#!/home/pi/.rbenv/shims/ruby
# -*- coding: utf-8 -*-
require 'webrick'


# :CGIInterpreterを入れないと"cgi_runner.rb:46"でエラー発生。
server = WEBrick::HTTPServer.new({:BindAddress => '0.0.0.0', :Port => 80, :CGIInterpreter =>"/home/pi/.rbenv/shims/ruby"})

server.mount('/', WEBrick::HTTPServlet::FileHandler, Dir.pwd + "/htdocs")
#server.mount('/test.cgi', WEBrick::HTTPServlet::CGIHandler,  'test.rb')
server.mount_proc('/cgi-bin') do |req, res|
  WEBrick::HTTPServlet::CGIHandler.new(server, Dir.pwd + "/cgi-bin" + req.path_info).service(req, res) 
end

trap(:INT) do
  puts "STOP HTTPServer"
  server.shutdown
end


server.start

