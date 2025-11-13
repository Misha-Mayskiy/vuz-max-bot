import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Panel, Container, Grid, Button, Typography, Flex } from '@maxhub/max-ui';
import Input from '../components/Input';
import { useAuth } from '../contexts/AuthContext';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(username, password);
      navigate('/');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Ошибка входа. Проверьте логин и пароль.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Panel mode="secondary" style={{ minHeight: '100vh', padding: '20px' }}>
      <Container>
        <Grid gap={24} cols={1}>
          <Flex direction="column" align="center" gap={16}>
            <Typography.Title variant="large-strong">Вузуслуги</Typography.Title>
            <Typography.Action color="secondary">
              Войдите в систему для доступа к сервисам
            </Typography.Action>
          </Flex>

          <form onSubmit={handleSubmit}>
            <Grid gap={16} cols={1}>
              <div>
                <Input
                  label="Логин"
                  labelColor="#ffffff"
                  placeholder="Введите логин"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              <div>
                <Input
                  label="Пароль"
                  labelColor="#ffffff"
                  type="password"
                  placeholder="Введите пароль"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>

              {error && (
                <Typography.Action color="danger" variant="small">
                  {error}
                </Typography.Action>
              )}

              <Button type="submit" disabled={loading} style={{ width: '100%' }}>
                {loading ? 'Вход...' : 'Войти'}
              </Button>
            </Grid>
          </form>
        </Grid>
      </Container>
    </Panel>
  );
}

export default LoginPage;

