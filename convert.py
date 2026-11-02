import os

def main():
    # 锁定你在国内配合播放时使用的真实本地域名（保持原样，走你本地的软路由或客户端分流代理）
    target_domain = "caonima.898757.xyz"
    
    # ===================================================================
    # 核心步骤：请将你在本地（挂着VPN时）在浏览器里打开并复制出来的
    # 完整的、上千行的真实 IPTV 列表文本，全部粘贴到下面这三个双引号之间！
    # ===================================================================
    raw_m3u_text = """#EXTM3U x-tvg-url="http://caonima.898757.xyz/sub/Zz0uFf9Cz0kp/epg.xml.gz"
#EXTINF:-1 tvg-id="stream-f4f9499d-607b-40aa-8fee-f10f774b13c3" tvg-name="YOG CH01" group-title="🏅青奥会",YOG CH01
http://caonima.898757.xyz/l/NUNiA3nqpusEnsNkG0wRmCbxb8d_5dfUpWPXP58gO1mhXlK0h8oWaExF9Tqbt94g/index.m3u8
#EXTINF:-1 tvg-id="stream-aaab82dd-07cb-4b46-95ce-24f6dc407386" tvg-name="YOG CH01(备用)" group-title="🏅青奥会",YOG CH01(备用)
http://caonima.898757.xyz/l/HhULA3tBTUX4VQ-9BBQZxDoZO9yuPn9L3aK1KboE1R_YT69FV24UxXdZ9xXW1EiB/index.m3u8
#EXTINF:-1 tvg-id="stream-d1b25850-4e95-4818-b546-fe6543b6d70a" tvg-name="YOG CH02" group-title="🏅青奥会",YOG CH02
http://caonima.898757.xyz/l/v4qPR-0L0A_eKV9nmz3W6fmoIhXSxH9UR0_d9Tdna7KxZkZitu-DzlDUnpKKSTof/index.m3u8
#EXTINF:-1 tvg-id="stream-4c960181-dece-4afa-baa7-bdaf972134f0" tvg-name="YOG CH02(备用)" group-title="🏅青奥会",YOG CH02(备用)
http://caonima.898757.xyz/l/6gku4F04-YtBW68eMOkxtoTX2aKu999REak0Zf4Nio9i2UM_oP8ehoj4dPwVXi1m/index.m3u8
#EXTINF:-1 tvg-id="stream-dfa28822-603e-450c-90cb-40c39c636f3b" tvg-name="YOG CH03" group-title="🏅青奥会",YOG CH03
http://caonima.898757.xyz/l/YRj0CdNIkEM4QqXJxFfGKC-UJ0iqcjoRfyx4Jcd4x2D6Ma7lhLs-_2CerFEINnSL/index.m3u8
#EXTINF:-1 tvg-id="stream-483d60d7-0ff7-4eb2-92fd-a2c6e407172e" tvg-name="YOG CH03(备用)" group-title="🏅青奥会",YOG CH03(备用)
http://caonima.898757.xyz/l/TLx2eQ3oxOFiAgbBmmKzVhvlXZQB5MM5DRDDQijD5zG1hAaW1VpXnRXi2wat3Fdc/index.m3u8
#EXTINF:-1 tvg-id="stream-c908dede-1068-4d44-b547-b381646cf0a0" tvg-name="YOG CH04" group-title="🏅青奥会",YOG CH04
http://caonima.898757.xyz/l/fqiH9dpJyYrKqvQBCu8hsBjdecSlVo0BIv4u12sBcvIMhbCCrh_zTDBgUuukyrap/index.m3u8
#EXTINF:-1 tvg-id="stream-64c6b720-7056-4896-9bf1-13ba993c11d0" tvg-name="YOG CH04(备用)" group-title="🏅青奥会",YOG CH04(备用)
http://caonima.898757.xyz/l/oLnueuYPrWU4p8DtlfYNZNcj81rWV1mLGhMpJckyBO_zenriOC0zOr2WCjG4lE4I/index.m3u8
#EXTINF:-1 tvg-id="stream-abf82a35-eba2-47b9-b294-f970301bba0c" tvg-name="YOG CH05" group-title="🏅青奥会",YOG CH05
http://caonima.898757.xyz/l/RDpgabEZRUkS0Hqkjao4WAsSP0JK-nspNGOnijz3jR9uWWORNtzuOQgzxBtn9swT/index.m3u8
#EXTINF:-1 tvg-id="stream-6d46cbfb-3cfb-44d6-8dc9-56c38b4894ee" tvg-name="YOG CH05(备用)" group-title="🏅青奥会",YOG CH05(备用)
http://caonima.898757.xyz/l/aOLeMqPxmJKrQiaAyShqXP4n-EwLCE5JynVesHoVX9uw9jQtgaRr7e4VZ2Z3BANd/index.m3u8
#EXTINF:-1 tvg-id="stream-2aebe294-1ad4-4cb1-a653-5e850be7ab98" tvg-name="YOG CH06" group-title="🏅青奥会",YOG CH06
http://caonima.898757.xyz/l/nsMF0dpex-hC_A8qxpgEPNn6PLnMLlcvkWXzawVafFoW2dRGcAmYGyl_wvtyUWB7/index.m3u8
#EXTINF:-1 tvg-id="stream-041ef399-ed4a-417d-8900-ca2ec9a80da7" tvg-name="YOG CH06(备用)" group-title="🏅青奥会",YOG CH06(备用)
http://caonima.898757.xyz/l/7PY8W1asBnCwSEkn-Vo-whwV1lLI1x5YihyVvX8NsDyGZgGhUaP1_CizDmMVshVC/index.m3u8
#EXTINF:-1 tvg-id="stream-09d8c476-e73d-45ea-99fd-d574f576cd08" tvg-name="HOY TV" tvg-logo="https://epg.v1.mk/logo/hoytv.png" group-title="🇭🇰 香港频道",HOY TV
http://caonima.898757.xyz/l/sueFnqNhKzPbQmmn-ohnxWdxl4N5A0XUxmUtXC3eOFUOnDm8dQRn28WZwdDvjtIN/index.m3u8
#EXTINF:-1 tvg-id="stream-1da6bd90-ffe9-4c30-8ab4-b0d9c6eb7898" tvg-name="HOY资讯台" tvg-logo="https://epg.v1.mk/logo/hoy资讯台.png" group-title="🇭🇰 香港频道",HOY资讯台
http://caonima.898757.xyz/l/r5oOU8dcVIKbexO7SMncD_f0HlDg4U8eZR5T5BvMxltYB6EXsRCS89fivTaie7qU/index.m3u8
#EXTINF:-1 tvg-id="stream-e99bd9b2-cd09-4f71-9e22-7965694c3c3e" tvg-name="NOW新闻台" tvg-logo="https://epg.v1.mk/logo/now新闻台.png" group-title="🇭🇰 香港频道",NOW新闻台
http://caonima.898757.xyz/l/OeXbj_L--PFW0OGxH3TRaacXO4P32Md1NcbObYo3qS4tk0SGPiaM9ECTvLTagLmP/index.m3u8
#EXTINF:-1 tvg-id="stream-df166b2f-51a5-4347-88e2-f71dadb06c19" tvg-name="凤凰中文" tvg-logo="https://epg.v1.mk/logo/凤凰中文.png" group-title="🇭🇰 香港频道",凤凰中文
http://caonima.898757.xyz/l/CCS2Dywd11Nfz558QSIxYOgVMBQcSDy3dki6hOct9j1Vc-aWspWNepSYXHpUgHiM/index.m3u8
#EXTINF:-1 tvg-id="stream-1021f7e2-5888-4900-a1e9-3a74365cb198" tvg-name="凤凰资讯" tvg-logo="https://epg.v1.mk/logo/凤凰资讯.png" group-title="🇭🇰 香港频道",凤凰资讯
http://caonima.898757.xyz/l/QrK9mDo1AKKpqDyB36_0wdnWE7irPD5ExBxwYxR7zSq2L6u_t1NmXUaJJMs0mo-D/index.m3u8
#EXTINF:-1 tvg-id="stream-9af9f54c-6939-4167-bc16-5b007c6e3724" tvg-name="凤凰香港" tvg-logo="https://epg.v1.mk/logo/凤凰香港.png" group-title="🇭🇰 香港频道",凤凰香港
http://caonima.898757.xyz/l/Fzj-Mxli_e0MgKO8RPvNNoX-ZdeEiLI-6Gszewd5fniRKoLKNvyT7YIbbGm2-Iwb/index.m3u8
#EXTINF:-1 tvg-id="stream-5929ffa2-0fe7-4200-9415-fec8470d4044" tvg-name="翡翠台" tvg-logo="https://php.946985.filegear-sg.me/logo/翡翠台.png" group-title="🇭🇰 香港频道",翡翠台
http://caonima.898757.xyz/l/HvDtxkzw6ZxnJVlQX0N--WVH-_URUDs3nb_qIa7sgHy2GBvmaWRtX72P08dKrkkc/index.m3u8
#EXTINF:-1 tvg-id="stream-a4f08b46-16f7-43ba-8bb9-6f139a341f6c" tvg-name="翡翠台 4K" tvg-logo="https://php.946985.filegear-sg.me/logo/翡翠台.png" group-title="🇭🇰 香港频道",翡翠台 4K
http://caonima.898757.xyz/l/dQK86V9hf9FuDPMpsmBj70RiEYVM-plaA98RKYppJMNKzlHpA0Tua0RoFzBd11EG/index.m3u8
#EXTINF:-1 tvg-id="stream-c92b7492-2a14-459f-8f06-88143a341b79" tvg-name="TVB Plus" tvg-logo="https://php.946985.filegear-sg.me/logo/TVBPlus.png" group-title="🇭🇰 香港频道",TVB Plus
http://caonima.898757.xyz/l/RWJSZyf4gwP8CxgkOT5ledScXtHclUYdygC4cpQWPwJCXznYTSBiAbWGUQCk3IPT/index.m3u8
#EXTINF:-1 tvg-id="stream-76049b75-00f3-4eee-b193-306f32742fd1" tvg-name="無綫新聞台" tvg-logo="https://php.946985.filegear-sg.me/logo/無綫新聞台.png" group-title="🇭🇰 香港频道",無綫新聞台
http://caonima.898757.xyz/l/6FcD7JoTP1x6pd2oK23az21I0ldDva1sx5-FmuxGa3O1fQE7MvvcdRvvY3tby-7C/index.m3u8
#EXTINF:-1 tvg-id="stream-3b4e154d-b864-4d71-90a7-b9fcc5fd2115" tvg-name="明珠台" tvg-logo="https://php.946985.filegear-sg.me/logo/明珠台.png" group-title="🇭🇰 香港频道",明珠台
http://caonima.898757.xyz/l/fJR3i3ETD3OJLy0h-uM6dxsSZ0jDX-GAvbhC8dDWmUnPGmphyPGYKJY5x64PutSf/index.m3u8

"""
    # ===================================================================
    
    if "#EXTM3U" not in raw_m3u_text:
        print("提示: 列表中没有找到标准的 EXTM3U 头部，请检查上面的粘贴内容！")
        return

    print("正在通过 GitHub Actions 内存进行全自动标准协议防封指令注入...")
    
    lines = raw_m3u_text.split('\n')
    new_lines = []
    
    for line in lines:
        if line.startswith("#EXTINF"):
            new_lines.append(line)
            # 在每一个频道下方强行插入 VLC/PotPlayer 特征伪装指令
            # 这能强制让国内电视和电脑在建立连接时带上完美的 Chrome 指纹，直接冲破对方的第一层阻断
            new_lines.append('#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
        else:
            # 保持原多层嵌套域名不变，直接在本地完美适配你的 VPN 分流
            original_domain = "caonima.898757.xyz"
            rewritten_line = line.replace(f"http://{original_domain}", f"https://{target_domain}")
            new_lines.append(rewritten_line)
            
    rewritten_content = '\n'.join(new_lines)

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"【大功告成】本地清洗与批量重组成功！文件已保存为: {output_path}")

if __name__ == "__main__":
    main()
