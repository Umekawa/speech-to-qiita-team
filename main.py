import sys
import qiita_team
import text_to_audio

if __name__ == '__main__':
  audio_file_path = sys.argv[1]
  article_body = text_to_audio.get_text(audio_file_path)
  qiita_team.post_qiita_team(audio_file_path, article_body)
