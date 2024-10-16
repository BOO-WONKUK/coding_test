def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    def time(s):
        a,b = map(int, s.split(':'))
        return a*60 + b
    vi_len = time(video_len)
    op_s = time(op_start)
    op_e = time(op_end)
    po = time(pos)
    if op_s <= po <= op_e:
        po = op_e
    for k in commands:
        if k == 'next':
            
            if vi_len - po <= 10:
                po = vi_len
            else:
                po += 10
            if op_s <= po <= op_e:
                po = op_e
        elif k == 'prev':
            if po <= 10:
                po = 0
            else:
                po -= 10
            if op_s <= po <= op_e:
                po = op_e
    h = po//60
    m = po % 60
    if h < 10:
        h_s = '0' + str(h)
    else:
        h_s = str(h)
    if m < 10:
        m_s = '0' + str(m)
    else:
        m_s = str(m)
    
    answer += h_s + ':' + m_s
    return answer