import jaynes

from launch_entry import train_fn

if __name__ == "__main__":
    hosts = [
        'vision03',
        'vision04',
        # 'visiongpu003',
    ]

    for host in hosts:
        jaynes.config(verbose=False, launch=dict(ip=host))
        jaynes.run(train_fn)

    # jaynes.listen(200)
