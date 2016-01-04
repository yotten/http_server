#!/home/pi/.rbenv/shims/ruby
# -*- coding: utf-8 -*-
require "cgi"

@filename = 'data.txt'

def writeHeader
  puts "Content-Type: text/html"
  puts
  puts "<html><head>"
  puts "<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\">"
  puts "</head><body>"
  puts "<table width=600><tr bgcolor=#FFCCCC><td>一言掲示板</td></tr>"
  puts "<tr><td> </td></tr>"
end

def writeFooter
  puts "<tr><td><hr></td></tr>"
  puts "<tr><td style=\"font-size:9pt;text-align:right;\">copyright yotten</td><tr>"
end

def writeForm
  puts <<EOF
<tr><td>
<table>
  <form method="POST" action="dengon.cgi">
  <tr>
    <td>タイトル</td><td><input type="text" name="title" size="20"></td>
  </tr>
  <tr>
    <td>内容</td><td><input type="text" name="honbun" size="60"></td>
  </tr>
  <tr>
    <td></td><td><input type="submit" value="送信"></td>
  </tr>
  </form>
</table>
</td></tr>
<tr><td><hr></td></tr>
EOF

end

def readFromFile(f)
  data = {}

  begin
    file = File.open(f)
    while (str = file.gets)
      str = str.chomp
      arr = str.split("\t")
      data.store(arr[0], arr[1])
    end
  rescue Exception => e
    puts "データファイルのオープンに失敗しました。ファイルが存在しないようです。(" + e.message + ")"
  ensure
    file.close if file != nil
  end

  return data
end

def saveToFile (f, data)
  begin
    file = File.open(f, "w")
    file.flock(File::LOCK_EX)
    data.each do |key, obj|
      file.puts key + "\t" + obj
    end
  rescue Exception => e
    puts "何らかの原因でデータの保存に失敗しました。(" + e.message + ")"
    return
  ensure
    if file != nil
      file.flock(File::LOCK_UN)
      file.close
    end
  end
end

def writeData
  data = readFromFile(@filename)
  puts "<tr><td>"
  puts "<table border=1 width=100%>"
  puts "<th width=20%>タイトル</th><th width=80%>内容</th>"
  data.each do |title, honbun|
    puts "<tr>"
    puts "<td>" + title + "</td>"
    puts "<td>" + honbun + "</td>"
    puts "</tr>"
  end
  puts "</table>"
  puts "</td><tr>"
end
def checkForm
  cgi = CGI.new

  if cgi.has_key?('title')
    title = cgi['title']
    honbun = cgi['honbun']
    data = readFromFile(@filename)
    data.store(title, honbun)
    saveToFile @filename,data
  end
end

writeHeader
checkForm
writeForm
writeData
writeFooter

