#!/usr/bin/env ruby

class AFshell
  
  def initialize(command, parameter)
  end
  
  def exploit
  end
  
  def help
  end
  
  def show
  end
  
  def select
  end
  
  def exit
  end
  
  def quit
    Process.exit!
  end
  
  def version
    puts " "
    puts "  Ameba Framework 0.1.1"
    puts "  Copyright -c- 2009"
    puts "  Carlos A. Lozano <vendetta@bugcon.org>"
    puts " "
  end
  
  def execute_command
    if @command=="help"
      self.help
    elsif @command=="show"
      self.show
    elsif @command=="select"
      self.select
    elsif @command=="version"
      self.version
    elsif @command=="exit"
      self.exit
    elsif @command=="quit"
      self.quit
    elsif @command=="exploit"
      self.exploit
    elsif @command==nil
      # Nothing here...
    else
      puts " "
      puts "ERROR: Command not found, please try again..."
      puts " "
    end
  end
end
