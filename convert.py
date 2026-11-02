import os
import urllib.request
import ssl
import base64
import socket

def main():
    # 1. 彻底锁定正确的原始抓取源链接
    source_url = "https://898757.xyz"
    
    # 2. 彻底锁定你在国内配合播放时要使用的域名（直接写死原域名，配合本地分流）
    target_domain = "caonima.898757.xyz"
    
    # 3. 严格锁死你德国节点的全部真实物理参数（确保没有符号干扰）
    proxy_host = "://oshuawei.com"
    proxy_port = 443
    proxy_user = "8cdb3920-978c-68f4-3d9a-0a41cbaeaaa5"
    proxy_pass = "8cdb3920-978c-68f4-3d9a-0a41cbaeaaa5"

    print("==================================================")
    print("【开始运行】标准 HTTPS 代理物理直连通道初始化...")
    print(f"当前固定抓取源: {source_url}")
    print(f"目标代理服务器域名: {proxy_host}")
    
    # 在微软云机房底层直接解析正确的德国长域名
    try:
        print("正在利用 GitHub 骨干网动态检索节点 IP...")
        proxy_ip = socket.gethostbyname(proxy_host)
        print(f"【成功】成功捕获德国节点公网实际 IP: {proxy_ip}")
    except Exception as dns_err:
        print(f"【DNS异常】尝试解析 {proxy_host} 失败: {dns_err}")
        print("由于该域名属于定制专线，现在强制切换到全网备用标准解析尝试握手...")
        # 如果由于机房限制无法解析该长域名，直接使用其同机房底层公网网关进行物理撞击
        proxy_ip = proxy_host 

    # 组装密文认证
    auth_str = f"{proxy_user}:{proxy_pass}"
    auth_encoded = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
    
    proxy_address = f"https://{proxy_ip}:{proxy_port}"
    proxy_handler = urllib.request.ProxyHandler({
        'http': proxy_address,
        'https': proxy_address
    })
    
    ssl_context = ssl._create_unverified_context()
    opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ssl_context))
    
    # 注入标准海外高匿名 Chrome 浏览器指纹与强力授权头部
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'),
        ('Accept-Language', 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7'),
        ('Proxy-Authorization', f"Basic {auth_encoded}"),
        ('Proxy-Connection', 'keep-alive'),
        ('Connection', 'keep-alive')
    ]
    urllib.request.install_opener(opener)

    print("--------------------------------------------------")
    print("正在通过加密隧道发起跨境请求，抓取原始 M3U 列表...")
    
    try:
        with urllib.request.urlopen(source_url, timeout=50) as response:
            m3u_content = response.read().decode('utf-8')
            print(f"【大获成功】原始播放列表成功拉回！数据体积: {len(m3u_content)} 字节")
    except Exception as fetch_err:
        raise Exception(f"致命错误：虽然IP正确，但节点拒绝了连接或返回了错误。原因: {fetch_err}")

    print("--------------------------------------------------")
    print("正在全自动执行本域静态地址重写重组...")
    original_domain = "caonima.898757.xyz"
    rewritten_content = m3u_content.replace(f"http://{original_domain}", f"https://{target_domain}")
    rewritten_content = rewritten_content.replace(f"https://{original_domain}", f"https://{target_domain}")

    output_path = "live.m3u"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rewritten_content)
    
    print(f"静态转换成功，已物理生成本地文件: {output_path}")
    print("==================================================")

if __name__ == "__main__":
    main()

