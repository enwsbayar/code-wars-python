# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def makeReadable(seconds):

  minutes = seconds//60
  seconds = seconds%60

  hours  = minutes//60
  minutes = minutes%60

  if hours < 10:
    hours = "0{}".format(hours)

  if minutes < 10:
    minutes = "0{}".format(minutes)

  if seconds < 10:
    seconds = "0{}".format(seconds)

  return "{}:{}:{}".format(hours,minutes,seconds)

print(makeReadable(86400))