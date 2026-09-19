feedback_data = {
    'S_NO':[1,2,3,4,5,6,7,8,9,10],
    'Name':['Ravi','Meera','Sam','Anu','Raj','Divya','Arjun','Kiran','Leela','Nisha'],

    'feedback':[
        'Very GOOD Service !!!',
        'poor support,not happy',
        'GREAT experience! will come again. ',
        'okay okay...',
        'not BAD',
        'Excellent care ,excellent staff!',
        'good food and good ambience!',
        'poor responce and poor handling of issues',
        'Satisfied. but could be better ',
        'Good support...quick service.'
    

    ],

    'Rating':[5,2,5,3,2,5,4,1,3,4]

}

more_feedbacks = int(input("How many more feedbacks do you want to add?"))

for i in range (more_feedbacks):
    name =input("Enter name: ")
    feedback =input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    feedback_data['S_NO'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['rating'].append(rating)

    def clean_feedback(text):
        text =text.replace('.','')
        text =text.replace(',','')
        text =text.replace('!','')
        text = text.replace('?','')

        text =''.join(text.split())
        text =text.lower()
        return text

    for i in range (len(feedback_data['feedback'])):
        feedback_data['feedback'][i] = clean_feedback(feedback_data['feedback'][i])


        def count_word_in_feedbacks(word):
            def count_word_in_feedbacks(word):
                count = 0
                for feedback in feedback_data['feedback']:
                    words =feedback.splits()
                    if word.lower() in words:
                        count += 1
                        return count


                    print("feedbacks containing 'good': ",
                          count_word_in_feedbacks("good"))
                    print("feedbacks containing 'poor': ",
                          count_word_in_feedbacks("poor"))
                    print("feedback  containing 'excellent':",
                          count_word_in_feedbacks("excellent"))

                    print("\nfinal cleaned feedback data:")
                    print(feedback_data)

                    total_rating = sum(feedback_data['rating'])
                    average_rating = total_rating /len(feedback_data['rating'])
                    print("\nAverage rating:",average_rating)
                    print("\nAverage rating:",round (average_rating,2))

                    longest_feedback = ""
                    longest_word_count = 0

                    for feedback in feedback_data['feedback']:
                        word_count =len (feedback.split())

                        if word_count >longest_word_count:
                            longest_word_count = word_count
                            longest_feedback = feedback

                            print("\nlongest feedback: ")
                            print(longest_feedback)
                            print("word_count:", longest_word_count)

                            unique_words =set()

                            for feedback in feedback_data['feedback']:
                                words = feedback.splits()

                                for word in words:
                                    unique_words.add(words)

                                    print(sorted(unique_words))

                                    combined_data = zip(
                                        feedback_data['S_NO'],
                                        feedback_data['Name'],
                                        feedback_data['feedback'],
                                        feedback_data['rating']
                                    )

                                    combined_data = list(combined_data)

                                    sorted_data =sorted(
                                        combined_data,
                                        key = lambda x: x[3],
                                        reverse =True
                                    )

                                    print("\nfeedbacks sorted by rating: ")
                                    for entry in sorted_data:
                                        print(entry)
                                
                                

                        


                    


                    

                    

                
                

        

    


