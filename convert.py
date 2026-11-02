import os
import urllib.request
import socks  # 稍后在工作流中通过 pip 安装
from sockshandler import SocksiPyHandler

def main():
    source_url = os.environ.get("SOURCE_M3U_URL")
    target_domain = os.environ.get("TARGET_PROXY_DOMAIN")
    
    if not source_url:
        print("错误: 未配置 SOURCE_M3U_URL")
        return

    print("正在通过本地 NaiveProxy (SOCKS5://127.0.0.1:1080) 抓取原始 M3U 列表中...")
    
    # 强制让所有 urllib 请求通过后台运行的本地 NaiveProxy 中转
    opener = urllib.request.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080))
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'),
        ('Accept', '*/*'),
        ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8')
    ]
    urllib.request.install_opener(opener)

    try:
        with urllib.request.urlopen(source_url, timeout=30) as response:
            m3u_content = response.read().decode('utf-8')
            print("原始列表抓取成功！")
    except Exception as e:
        print(f"抓取失败: {e}")
        return

    print(f"开始重写媒体流链接，目标本地域名/中转路径: {target_domain}")
    
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"列表重写完成！已成功保存为静态文件: {output_path}")

if __name__ == "__main__":
    main()
