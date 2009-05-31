if ARGV.length.to_i==0
    puts " "
    puts "             ,,,,,,,,"
    puts "           ,|||````||||"
    puts "     ,,,,|||||       ||,"
    puts "  ,||||```````       `||"
    puts ",|||`                 |||,"
    puts "||`     ....,          `|||"
    puts "||     ::::::::          |||,"
    puts "||     :::::::'     ||    ``|||,"
    puts "||,     :::::'               `|||"
    puts "`||,                           |||"
    puts " `|||,       ||          ||    ,||"
    puts "   `||                        |||`"
    puts "    ||                   ,,,||||"
    puts "    ||              ,||||||```"
    puts "   ,||         ,,|||||`"
    puts "  ,||`   ||   |||`"
    puts " |||`         ||"
    puts ",||           ||"
    puts "||`           ||"
    puts "|||,         |||"
    puts " `|||,,    ,|||"
    puts "   ``||||||||`"
    puts " "
    puts " "

  while true
    printf("AFshell > ")
    STDOUT.flush
    input=gets.chomp
    command, parameter=input.split(" ")
  
    current_afShell=afshell.new(command, parameter)
    current_afShell.execute_command()
  end
  
else
  #Speed launcher
end
