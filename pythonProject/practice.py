# 사각형 그리기 게임
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_area = 0
    cnt = 0
    for r1 in range(N):
        for c1 in range(N):
            for r2 in range(r1, N):
                for c2 in range(c1, N):
                    if arr[r1][c1] == arr[r2][c2]:
                        height = r2 - r1 + 1
                        width = c2 - c1 + 1
                        area = height * width
                        if area > max_area:
                            max_area = area
                            cnt = 1
                        elif area == max_area:
                            cnt += 1
    print(f'#{tc} {cnt}')
