from rest_framework import serializers
from .models import Article, Comment

# serializer : 직렬화
# django data를 json으로 바꿔준다

# 전체 게시글 직렬화
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )

# 단일 게시글 직렬화
class ArticleSerializer(serializers.ModelSerializer):
    # 게시글 하나(1) : 댓글들(N)
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = (
                'id',
                'content',
            )

        # 읽기 전용 필드(read_only=True)
        # 1. 사용자로부터 입력받지 않음
        # 2. 유효성 검사 과정에서 제외
        # 3. 입력받지는 않지만 결과는 클라이언트에 제공
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    # comment_set : 역참조, count : 메서드
    comment_count = serializers.IntegerField(
        source = 'comment_set.count', read_only = True
    )
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # 1. 댓글을 조회했을 때 게시글의 제목도 같이 나오게
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
        # 댓글 조회했을 때 같이 응답하는 게시글의 제목은 읽기 전용
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'