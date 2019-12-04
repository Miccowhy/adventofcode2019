doubledigit(password) = true in (password[i] == password[i+1] for i in 1:5)
ascending(password) = !(false in (password[i] <= password[i+1] for i in 1:5))

println(sum(doubledigit(string(password)) && ascending(string(password)) for password in 146810:612564))
