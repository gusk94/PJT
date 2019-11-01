from django.contrib import admin
from .models import Movie

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_en')
    # movie = Movie()
    # movie.title = '엑시트'
    # movie.title_en = 'EXIT'
    # movie.audience = 2962455
    # movie.open_date = '2019-07-31'
    # movie.genre = '코미디'
    # movie.watch_grade = '12세이상관람가'
    # movie.score = '9.07'
    # movie.poster_url = 'https://movie-phinf.pstatic.net/20190724_161/1563931152464tk11A_JPEG/movie_image.jpg'
    # movie.description = '짠내 폭발 청년백수, 전대미문의 진짜 재난을 만나다! 대학교 산악 동아리 에이스 출신이지만  졸업 후 몇 년째 취업 실패로 눈칫밥만 먹는 용남은  온 가족이 참석한 어머니의 칠순 잔치에서  연회장 직원으로 취업한 동아리 후배 의주를 만난다  어색한 재회도 잠시, 칠순 잔치가 무르익던 중  의문의 연기가 빌딩에서 피어 오르며  피할 새도 없이 순식간에 도심 전체는 유독가스로 뒤덮여 일대혼란에 휩싸이게 된다.  용남과 의주는 산악 동아리 시절 쌓아 뒀던 모든 체력과 스킬을 동원해  탈출을 향한 기지를 발휘하기 시작하는데…'
    
    # movie.save()

    # movie = Movie()
    # movie.title = '사자'
    # movie.title_en = 'The Divine Fury'
    # movie.audience = 1167334
    # movie.open_date = '2019-07-31'
    # movie.genre = '미스터리'
    # movie.watch_grade = '15세관람가'
    # movie.score = '8.32'
    # movie.poster_url = 'https://movie-phinf.pstatic.net/20190625_168/1561426986010A3uBi_JPEG/movie_image.jpg'
    # movie.description = '어릴 적 아버지를 잃은 뒤 세상에 대한 불신만 남은 격투기 챔피언 ‘용후’(박서준).   어느 날 원인을 알 수 없는 깊은 상처가 손바닥에 생긴 것을 발견하고,  도움을 줄 누군가가 있다는 장소로 향한다.  그곳에서 바티칸에서 온 구마사제 ‘안신부’(안성기)를 만나   자신의 상처 난 손에 특별한 힘이 있음을 깨닫게 되는 ‘용후’.   이를 통해 세상을 혼란에 빠뜨리는 악(惡)의 존재를 알게 되고,  강력한 배후이자 악을 퍼뜨리는 검은 주교 ‘지신’(우도환)을 찾아 나선 ‘안신부’와 함께 하게 되는데...!    악의 편에 설 것인가   악에 맞설 것인가   신의 사자가 온다!'
    
    # movie.save()