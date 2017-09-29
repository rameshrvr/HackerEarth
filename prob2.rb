limit = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}
output = 1
array.each.map{|x| output *= x}
(1..(limit-1)).each do |x|
	puts x if (x ** array.length) > output
end