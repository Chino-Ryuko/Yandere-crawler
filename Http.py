import urllib.request

def get(url: str, header: list = {}):
    """
    HTTP GET获取
    :param url: URL地址
    :param header: HTTP头
    :return: row
    """
    header['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    header['Accept-Language'] = 'zh-CN,zh;q=0.8,en;q=0.6'
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2883.103 Safari/537.36'
# 增加Cookie登陆
    header['Cookie'] = 'vote=1; pass_hash=caded337d418034731e6891f0151d21e2a8b32e8; login=chino_ryuko; user_id=306084; user_info=306084%3B30%3B1; has_mail=0; comments_updated=1; block_reason=; resize_image=0; show_advanced_editing=1; my_tags=; held_post_count=0; forum_post_last_read_at=%222017-06-28T11%3A56%3A13.204Z%22; reported_error=1; mode=view; tag-script=; country=JP; yande.re=RVVCZi9rTGkzVW1nUHFPaUlYcktkUG0xNVlqVFMzZG5iaFlGWFkrdHJFSitYMGxOY3NDcEZIdDUyN0dyd2dlS2JMZ09NZkZPVnl3TzR4NnA4Mm41YlEwenk1MkhYS3ZqRm03MXRnQStvSHpQemNmWFFCcEIydGtBblV2YXIyaTBYeEFrZjNOdlhTQTduMk1QK0phOEZUQk5OdGUwQ3VicmV1eUhId0U0NGRCSlFrYzRzM25jZ1Z1SDYwZ0d2NStuVUdLVFRzN2c1Q3pPMnVxTWlOeW9sZz09LS1zOERVd2V6aVlOZHVtcWZrT2pjNG9nPT0%3D--d616e03ea9fb83a0d4de715828b368f66990694f'
    req = urllib.request.Request(url, headers=header)
    return urllib.request.urlopen(req).read()



