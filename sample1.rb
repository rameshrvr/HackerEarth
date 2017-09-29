cipher = {}
data = []
(1..26).each do |x|
  ('a'..'z').map { |y| cipher[y] = x }
end
test_cases = gets.strip.to_i
(0...test_cases).each do |x|
  data[x] = gets.strip
end
(0...test_cases).each do |y|
  temp = data[y].reverse
  result = 1
  if temp == data[y]
    puts 'Palindrome'
    next
  end
  temp1 = data[y].split('')
  temp1.map { |x| result *= cipher[x] }
  print result
end
