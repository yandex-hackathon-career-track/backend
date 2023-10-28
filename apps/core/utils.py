from datetime import date


def calculate_total_experience(self):
    """Расчет общего опыта."""
    total_experience = 0
    job_dates = []

    for job in self.jobs.all():
        experience_months = job.experience

        for existing_job_dates in job_dates:
            if (
                job.start_date <= existing_job_dates[1]
                and job.end_date >= existing_job_dates[0]
            ):
                overlapping_start = max(job.start_date, existing_job_dates[0])
                overlapping_end = min(job.end_date, existing_job_dates[1])
                experience_months -= (
                    overlapping_end - overlapping_start
                ).days // 30

        if experience_months > 0:
            total_experience += experience_months
            job_dates.append((job.start_date, job.end_date))

    return total_experience


def calculate_job_experience(start_date, end_date, is_current):
    """Расчет оыта от даты начала работы."""
    if is_current:
        today = date.today()
        delta = today - start_date
    elif end_date:
        delta = end_date - start_date
    else:
        return 0

    months = delta.days // 30
    return months
