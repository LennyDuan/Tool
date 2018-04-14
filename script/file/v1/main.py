def map(transcript, mapper, template):
    code = transcript.code
    if mapper[code]:
        courseMapper = mapper[code]
        department = courseMapper.department
        equivalency = courseMapper.equivalency
        credits = courseMapper.credits

        for key, val in template.items():
            if(equivalency.upper() in key.upper()):
                print(courseMapper.toString())
                val.grade = credits
                break
    else:
        print('Cannot find the course' + transcript)
