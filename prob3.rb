cases = gets.strip.to_i
array = []
(0..cases-1).each do |x|
  array[x] = gets.strip.split(' ').map{|y| y.to_i}
end
array.each do |x|
	temp = x[0]
	(1..x[1]-1).each do
		temp = (temp ** x[0])
	end
	puts "#{temp%x[2]}"
end
