# Generated by Django 2.0.3 on 2018-11-18 11:22

import cyborgbackup.main.fields
import cyborgbackup.main.managers
import cyborgbackup.main.models.jobs
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDeprecatedStdout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_stdout_text', models.TextField(editable=False, null=True)),
            ],
            options={
                'db_table': 'main_job',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_agent', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', cyborgbackup.main.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('create', 'Entity Created'), ('update', 'Entity Updated'), ('delete', 'Entity Deleted'), ('associate', 'Entity Associated with another Entity'), ('disassociate', 'Entity was Disassociated with another Entity')], max_length=13)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('changes', models.TextField(blank=True)),
                ('object_relationship_type', models.TextField(blank=True)),
                ('object1', models.TextField()),
                ('object2', models.TextField()),
                ('setting', cyborgbackup.main.fields.JSONField(blank=True, default=dict)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity_stream', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('archive_name', models.CharField(max_length=1024)),
                ('mode', models.CharField(max_length=10)),
                ('path', models.CharField(max_length=2048)),
                ('owner', models.CharField(max_length=1024)),
                ('group', models.CharField(max_length=1024)),
                ('type', models.CharField(max_length=1)),
                ('healthy', models.BooleanField()),
                ('size', models.PositiveIntegerField()),
                ('mtime', models.DateTimeField()),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'catalog', 'model_name': 'catalog', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChannelGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200, unique=True)),
                ('channels', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('hostname', models.CharField(max_length=1024)),
                ('enabled', models.BooleanField(default=True)),
                ('ip', models.TextField(blank=True, default='')),
                ('version', models.CharField(blank=True, default='', max_length=50)),
                ('ready', models.BooleanField(default=False)),
                ('latest_prepare', models.DateTimeField(default=None, editable=False, null=True)),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'client', 'model_name': 'client', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'client', 'model_name': 'client', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=512)),
                ('inputs', cyborgbackup.main.fields.CredentialInputField(blank=True, default={}, help_text='Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credential', 'model_name': 'credential', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CredentialType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=512)),
                ('kind', models.CharField(choices=[('ssh', 'Machine'), ('net', 'Network'), ('scm', 'Source Control'), ('cloud', 'Cloud'), ('insights', 'Insights')], max_length=32)),
                ('inputs', cyborgbackup.main.fields.CredentialTypeInputField(blank=True, default={}, help_text='Enter inputs using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.')),
                ('injectors', cyborgbackup.main.fields.CredentialTypeInjectorField(blank=True, default={}, help_text='Enter injectors using either JSON or YAML syntax. Use the radio button to toggle between the two. Refer to the Ansible Tower documentation for example syntax.')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credentialtype', 'model_name': 'credentialtype', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credentialtype', 'model_name': 'credentialtype', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('kind', 'name'),
            },
        ),
        migrations.CreateModel(
            name='CyborgBackupScheduleState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_last_run', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=512)),
                ('job_type', models.CharField(choices=[('provision', 'Provision VM'), ('dns', 'Update DNS'), ('monit_observium', 'Monitoring Observium'), ('monit_status', 'Monitoring Status')], default='job', max_length=64)),
                ('old_pk', models.PositiveIntegerField(default=None, editable=False, null=True)),
                ('verbosity', models.PositiveIntegerField(blank=True, choices=[(0, '0 (Normal)'), (1, '1 (Verbose)'), (2, '2 (More Verbose)'), (3, '3 (Debug)'), (4, '4 (Connection Debug)')], default=0)),
                ('extra_vars', models.TextField(blank=True, default='')),
                ('timeout', models.IntegerField(blank=True, default=0, help_text='The amount of time (in seconds) to run before the task is canceled.')),
                ('emitted_events', models.PositiveIntegerField(default=0, editable=False)),
                ('launch_type', models.CharField(choices=[('manual', 'Manual'), ('relaunch', 'Relaunch'), ('callback', 'Callback'), ('scheduled', 'Scheduled'), ('dependency', 'Dependency'), ('workflow', 'Workflow'), ('sync', 'Sync'), ('scm', 'SCM Update')], default='manual', editable=False, max_length=20)),
                ('cancel_flag', models.BooleanField(default=False, editable=False)),
                ('status', models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('waiting', 'Waiting'), ('running', 'Running'), ('successful', 'Successful'), ('failed', 'Failed'), ('error', 'Error'), ('canceled', 'Canceled')], default='new', editable=False, max_length=20)),
                ('failed', models.BooleanField(default=False, editable=False)),
                ('started', models.DateTimeField(default=None, editable=False, help_text='The date and time the job was queued for starting.', null=True)),
                ('finished', models.DateTimeField(default=None, editable=False, help_text='The date and time the job finished execution.', null=True)),
                ('elapsed', models.DecimalField(decimal_places=3, editable=False, help_text='Elapsed time in seconds that the job ran.', max_digits=12)),
                ('job_args', models.TextField(blank=True, default='', editable=False)),
                ('job_cwd', models.CharField(blank=True, default='', editable=False, max_length=1024)),
                ('job_env', cyborgbackup.main.fields.JSONField(blank=True, default={}, editable=False)),
                ('job_explanation', models.TextField(blank=True, default='', editable=False, help_text="A status field to indicate the state of the job if it wasn't able to run and capture stdout")),
                ('start_args', models.TextField(blank=True, default='', editable=False)),
                ('result_traceback', models.TextField(blank=True, default='', editable=False)),
                ('celery_task_id', models.CharField(blank=True, default='', editable=False, max_length=100)),
                ('job_pool', models.IntegerField(blank=True, default=0)),
                ('original_size', models.BigIntegerField(default=0)),
                ('compressed_size', models.BigIntegerField(default=0)),
                ('deduplicated_size', models.BigIntegerField(default=0)),
                ('client', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_client', to='main.Client')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'job', 'model_name': 'job', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('dependent_jobs', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_blocked_jobs+', to='main.Job')),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'job', 'model_name': 'job', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            bases=(cyborgbackup.main.models.jobs.JobTypeStringMixin, models.Model),
        ),
        migrations.CreateModel(
            name='JobEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.CharField(default='', editable=False, max_length=1024)),
                ('parent_uuid', models.CharField(default='', editable=False, max_length=1024)),
                ('event', models.CharField(choices=[('debug', 'Debug'), ('verbose', 'Verbose'), ('deprecated', 'Deprecated'), ('warning', 'Warning'), ('system_warning', 'System Warning'), ('error', 'Error')], max_length=100)),
                ('event_data', cyborgbackup.main.fields.JSONField(blank=True, default={})),
                ('failed', models.BooleanField(default=False, editable=False)),
                ('changed', models.BooleanField(default=False, editable=False)),
                ('task', models.CharField(default='', editable=False, max_length=1024)),
                ('counter', models.PositiveIntegerField(default=0, editable=False)),
                ('stdout', models.TextField(default='', editable=False)),
                ('verbosity', models.PositiveIntegerField(default=0, editable=False)),
                ('start_line', models.PositiveIntegerField(default=0, editable=False)),
                ('end_line', models.PositiveIntegerField(default=0, editable=False)),
                ('job', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='job_events', to='main.Job')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=1024)),
                ('policy_type', models.CharField(choices=[('rootfs', 'Root FileSystem'), ('vm', 'Virtual Machine'), ('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('piped', 'Piped Backup'), ('config', 'Only /etc'), ('mail', 'Only mail directory')], default='rootfs', max_length=20)),
                ('enabled', models.BooleanField(default=True)),
                ('extra_vars', models.TextField(blank=True, default='')),
                ('mode_pull', models.BooleanField(default=False)),
                ('keep_hourly', models.IntegerField(default=None, null=True)),
                ('keep_daily', models.IntegerField(default=None, null=True)),
                ('keep_weekly', models.IntegerField(default=None, null=True)),
                ('keep_monthly', models.IntegerField(default=None, null=True)),
                ('keep_yearly', models.IntegerField(default=None, null=True)),
                ('next_run', models.DateTimeField(default=None, editable=False, help_text='The next time that the scheduled action will run.', null=True)),
                ('clients', models.ManyToManyField(to='main.Client')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'policy', 'model_name': 'policy', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'policy', 'model_name': 'policy', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=1024)),
                ('path', models.CharField(max_length=1024)),
                ('enabled', models.BooleanField(default=True)),
                ('repository_key', models.CharField(max_length=1024)),
                ('ready', models.BooleanField(default=False)),
                ('original_size', models.BigIntegerField(default=0)),
                ('compressed_size', models.BigIntegerField(default=0)),
                ('deduplicated_size', models.BigIntegerField(default=0)),
                ('latest_prepare', models.DateTimeField(default=None, editable=False, null=True)),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'repository', 'model_name': 'repository', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'repository', 'model_name': 'repository', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=1024)),
                ('crontab', models.CharField(max_length=1024)),
                ('enabled', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'schedule', 'model_name': 'schedule', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'schedule', 'model_name': 'schedule', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=None, editable=False)),
                ('modified', models.DateTimeField(default=None, editable=False)),
                ('key', models.CharField(max_length=255)),
                ('value', models.TextField(null=True)),
                ('setting_type', models.CharField(choices=[('boolean', 'Boolean'), ('integer', 'Integer'), ('string', 'String'), ('privatekey', 'Scheduled'), ('password', 'Dependency'), ('workflow', 'Workflow')], default='manual', editable=False, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='policy',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='main.Repository'),
        ),
        migrations.AddField(
            model_name='policy',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='main.Schedule'),
        ),
        migrations.AddField(
            model_name='job',
            name='policy',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='main.Policy'),
        ),
        migrations.AddField(
            model_name='job',
            name='repository',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_repository', to='main.Repository'),
        ),
        migrations.AddField(
            model_name='credential',
            name='credential_type',
            field=models.ForeignKey(help_text='Specify the type of credential you want to create. Refer to the Ansible Tower documentation for details on each type.', on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='main.CredentialType'),
        ),
        migrations.AddField(
            model_name='credential',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credential', 'model_name': 'credential', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='catalog',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogs', to='main.Job'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'catalog', 'model_name': 'catalog', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='client',
            field=models.ManyToManyField(blank=True, to='main.Client'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='job',
            field=models.ManyToManyField(blank=True, to='main.Job'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='policy',
            field=models.ManyToManyField(blank=True, to='main.Policy'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='repository',
            field=models.ManyToManyField(blank=True, to='main.Repository'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='schedule',
            field=models.ManyToManyField(blank=True, to='main.Schedule'),
        ),
        migrations.AddField(
            model_name='activitystream',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterIndexTogether(
            name='jobevent',
            index_together={('job', 'end_line'), ('job', 'event'), ('job', 'start_line'), ('job', 'uuid'), ('job', 'parent_uuid')},
        ),
        migrations.AlterUniqueTogether(
            name='credentialtype',
            unique_together={('name', 'kind')},
        ),
        migrations.AlterUniqueTogether(
            name='credential',
            unique_together={('name', 'credential_type')},
        ),
    ]