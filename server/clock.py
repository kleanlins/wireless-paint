frequency = 20

# simula um clock dado uma frequencia
# nao sei se precisaremos disso
def clock(freq):
    sleep_time = 1/freq
    while True:
        print("clock")
        sleep(sleep_time)


start_new_thread(clock,(frequency,))
sleep(1)
