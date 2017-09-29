num = gets.strip.to_i
array = gets.strip.split(' ').map{|x| x.to_i}
sum = 1
array.map{|y| sum *= y}
print sum