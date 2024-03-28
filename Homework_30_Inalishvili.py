# 1. შექმენი ასინქრონული event loop რომელიც ერთი წამის დაყოვნებით ამობეჭდავს რიცხვებს 1_დან 10_ის ჩათვლით.


import asyncio


async def main():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)


asyncio.run(main())




# 2. დაწერე ასინქრონული ფუნქციის კოდი, რომელიც მოიცდის ორი წამი და შემდეგ დაბეჭდავს "Hello World!!!"
# შექმენი event loop რომელიც ზემოხსენებულ ფუნქციას გაუშვებს.


import asyncio


async def arrested_printer():
    await asyncio.sleep(2)
    print("Hello World!")


async def main():
    task1 = asyncio.create_task(arrested_printer())
    await task1


asyncio.run(main())




# 3. ასინქრონული ჩატის კოდის (სერვერისა და კლიენტის) განხილვა


# server.py-ის კოდი
import asyncio

# ასინქრონული ფუნქცია, კლიენტისგან მიღებული მონაცემების წასაკითხად. ასინქრონულად ელოდება კლიენტის მონაცემებს 100 ბაიტის
# ფარგლებში, შემდეგ დეკოდირებას უკეთებს მიღებულ შეტყობინებას და ვრაითერ ობიექტისგან იღებს მისამართს, რათა უკან
# დაუბრუნოს ინფორმაცია შესაბამის კლიენტს.
async def handle_echo(reader, writer):
    print(reader)
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    # ელოდება, სანამ ინფორმაციის დამატება არ გახდება შესაძლებელი გასაგზავნად(ჩასაწერად).
    await writer.drain()

    print("Close the connection")
    # შემდეგ ხურავს კავშირს და ელოდება მის "ბოლომდე" დახურვას.
    writer.close()
    await writer.wait_closed()

# მთავარ ფუნქციაში უშვებს ასინქრონულ სერვერს, რომელიც არგუმენტად გადაცემულ აი პიზე და პორტზე "უსმენს" ინფორმაციის
# მიმოცვლას, რომელსაც შემდგომ handle_echo-ს საშუალებით "გაუმკლავდება".
async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)

    # იღებს სოკეტის მისამართებს, აერთებს ჩამონათვალს და პრინტავს კონსოლში.
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    # კონტექსტ მენეჯერი უზრუნველჰყოფს სერვერის სათანადოდ გაწმენდას??
    async with server:

        # იწყებს კლიენტების მოთხოვნების მომსახურებას განუსაზღვრელი დროით
        await server.serve_forever()

# ასინქრონული ივენთ ლუპი main ფუნქციის გასაშვებად.
asyncio.run(main())




# client.py-ის კოდი
import asyncio


# ასინქრონული ფუნქცია, მესიჯ პარამეტრით tcp კლიენტის სამართავად
async def tcp_echo_client(message):

    # ამყარებს კავშირს სერვერთან შესაბამის აიპისა და პორტზე, აბრუნებს ობიექტების წყვილს(სტრიმის წამკითხველს და ჩამწერს),
    # რომელთაც "ანფაქინგს" უკეთებს reader და writer ცვლადებში.
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    # პრინტავს სერვერისთვის გასაგზავნ მესიჯს
    print(f'Send: {message}')
    # ახდენს მესიჯის კოდირებას და წერს სერვერში writer ობიექტის მეშვეობით.
    writer.write(message.encode())
    # ელოდება პროცესის დასრულებას ახალი ინფორმაციის დასამატებლად.
    await writer.drain()

    # reader ობიექტის მეშვეობით კითხულობს სერვერისგან მიღებულ ინფორმაციას(100 ბაიტის მოცულობით).
    data = await reader.read(100)
    # მიღებულ ინფორმაციას დეკოდირებას უკეთებს, რათა კონსოლში დაბეჭდოს შესაბამისი ფორმატით.
    print(f'Received: {data.decode()!r}')

    # წყვეტს კავშირს და ელოდება პროცესების ბოლომდე დასრულებას.
    print('Close the connection')
    writer.close()
    await writer.wait_closed()

# ასინქრონული ივენთ ლუპი კლიენტის ფუნქციის გასაშვებად, რომელსაც საწყის მესიჯად გადაეცემა "Hello World!" სტრიქონი.
asyncio.run(tcp_echo_client('Hello World!'))
