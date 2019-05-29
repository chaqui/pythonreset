PASSWORD = '12345'

def password_requeried(func):
  def wrapper():
    password = input("Cual es tu contraseña?")
    if(password==PASSWORD):
      func()
    else:
      print('La contraseña no es correcta')

  return wrapper

def upper(func):
  def wrapper(*args, **kwargs):
    aa = []
    for arg in args: 
      aa.append(arg.upper())
      func("".join(aa), **kwargs)
  return wrapper


@password_requeried
def need_password():
  print('La contraseña es correcta')

@upper
def say_my_name(name):
  print('hola {}'.format(name))

if __name__=='__main__':
  need_password()
  say_my_name('Chaqui')