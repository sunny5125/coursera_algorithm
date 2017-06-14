class Karatsuba

  def self.product(x, y)
    x_string = x.to_s
    y_string = y.to_s

    n = [x_string.length, y_string.length].max
    if n == 1
      return x * y
    end

    middle = (n.to_f/2).ceil
    if n > x_string.length
      a = 0
      b = x
    else
      a = x_string[0...middle].to_i
      b = x_string[(middle)...x_string.length].to_i
    end

    if n > y_string.length
      c = 0
      d = y
    else
      c = y_string[0...middle].to_i
      d = y_string[(middle)...y_string.length].to_i  
    end

    # recursive calculations
    ac = product(a, c)
    bd = product(b, d)
    gauss_trick = product(a + b, c + d)

    gauss_trick = gauss_trick - ac - bd
  
    pow = n / 2
    pow = pow * 2

    return ac * (10 ** pow) + gauss_trick * (10 ** (pow / 2)) + bd

  end
end

# Input data:
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

# print out the result:
puts "\n X = #{x}"
puts " Y = #{y}"
puts "\n----------------------------------------------------------------------------------------------------------------------------------------"
puts " X * Y = #{Karatsuba.product(x,y)}"
puts "----------------------------------------------------------------------------------------------------------------------------------------\n"

#Output:8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
