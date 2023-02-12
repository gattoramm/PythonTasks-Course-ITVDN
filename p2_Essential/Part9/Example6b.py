# in applied code
handlers = []
for i in range(1, 4):
    def on_click(i=i):
        print('Button {} clicked!'.format(i))
    handlers.append(on_click)


# in event loop
for handler in handlers:
    handler()
