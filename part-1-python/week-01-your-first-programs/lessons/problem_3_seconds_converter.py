seconds = int(input("Seconds: "))
secs = seconds % 60
mins = (seconds - secs) % 3600 // 60
hrs = seconds // 3600
print(seconds, "seconds =", hrs, "h", mins, "min", secs, "s")